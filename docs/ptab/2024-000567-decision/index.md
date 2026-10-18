---
title: Ex parte Desjardins
citation: Ex parte Desjardins, 2024-000567, 2025-09-26 (precedential; designated 2025-11-04)
court_or_board: USPTO Appeals Review Panel
date: '2025-09-26'
docket_or_appeal_number: 2024-000567
precedential_status: precedential
designation_date: '2025-11-04'
de_designation_date: ''
topic_tags:
- Statutory subject matter
source_url: https://www.uspto.gov/sites/default/files/documents/202400567Ex_parte_Desjardins_arp_rehearing_decision.pdf
retrieved_on: '2026-10-17'
sha256: b0bd1059bc824a74c84f7b73c45a97877aaf9d007fec0799ceafcf7294443dd1
cited_by_stories:
- slug: d16-ai-claims-can-recite-math-and-still-pass-101
  url: https://postgrantproceeding.com/insights/d16-ai-claims-can-recite-math-and-still-pass-101
document_type: ptab
slug: 2024-000567-decision
paper: ''
related_dockets: []
designation_scope: ''
confirmation_status: confirmed
confirmation_note: ''
story_cite: Ex parte Desjardins, Appeal No. 2024-000567 (USPTO Appeals Review Panel
  September 26, 2025) (precedential, designated Nov. 4, 2025)
story_cite_match: true
mpep_revision: ''
original_file: original.pdf
legacy_release_file: 2025-09-26_ptab_2024-000567_ex-parte-desjardins.pdf
legacy_release_url: https://github.com/ssukduang-cpu/pgp-documents/releases/download/batch-2026-10-14/2025-09-26_ptab_2024-000567_ex-parte-desjardins.pdf
---

```json
{
  "@context": "https://schema.org",
  "@type": "Report",
  "name": "Ex parte Desjardins",
  "identifier": "Ex parte Desjardins, 2024-000567, 2025-09-26 (precedential; designated 2025-11-04)",
  "datePublished": "2025-09-26",
  "publisher": {
    "@type": "Organization",
    "name": "United States Patent and Trademark Office"
  },
  "url": "https://raw.githubusercontent.com/ssukduang-cpu/pgp-documents/master/docs/ptab/2024-000567-decision/index.md",
  "isBasedOn": "https://www.uspto.gov/sites/default/files/documents/202400567Ex_parte_Desjardins_arp_rehearing_decision.pdf",
  "encoding": {
    "@type": "MediaObject",
    "sha256": "b0bd1059bc824a74c84f7b73c45a97877aaf9d007fec0799ceafcf7294443dd1"
  }
}
```

Transcription of the official public record retrieved 2026-10-17. The file named in original_file is the retrieved original. The official source controls if this transcription differs.

## Text

UNITED STATES PATENT AND TRADEMARK OFFICE
                                                                             UNITED STATES DEPARTMENT OF COMMERCE
                                                                             United States Patent and Trademark Office
                                                                             Address: COMMISSIONERFORPATENTS
                                                                                     P.O. Box 1450
                                                                                      Alexandria, Virginia 22313-1450
                                                                                    www.uspto.gov

    APPLICATION NO.            FILING DATE           FIRST NAMED INVENTOR        ATTORNEY DOCKET NO.            CONFIRMATION NO.

       16/319,040              01/18/2019             Guillaume Desjardins           45288-8015US 1                     2007

       151793           7590            09/26/2025
                                                                                                      EXAMINER
       FISH & RICHARDSON P.C.
                                                                                                     TRIEU,EMN
       PO BOX 1022
       MINNEAPOLIS, MN 55440-1022
                                                                                         ART UNIT                 PAPER NUMBER

                                                                                            2128

                                                                                  NOTIFICATION DATE              DELIVERY MODE

                                                                                        09/26/2025                 ELECTRONIC

Please find below and/or attached an Office communication concerning this application or proceeding.

The time period for reply, if any, is set in the attached communication.

Notice of the Office communication was sent electronically on above-indicated "Notification Date" to the
following e-mail address(es):
PATDOCTC@fr.com

PTOL-90A (Rev. 04/07)

        UNITED STATES PATENT AND TRADEMARK OFFICE

           BEFORE THE APPEALS REVIEW PANEL OF THE
               PATENT TRIAL AND APPEAL BOARD

      Ex parte GUILLAUME DESJARDINS, RAZVAN PASCANU,
           RAIA THAIS HADSELL, JAMES KIRKPATRICK,
     JOEL WILLIAM VENESS, and NEIL CHARLES RABINOWITZ

                           Appeal2024-000567
                          Application 16/319,040
                          Technology Center 2100

Before JOHN A. SQUIRES, Under Secretary ofCommerce for Intellectual
Property and Director ofthe United States Patent and Trademark Office,
VALENCIA MARTIN WALLACE, Acting Commissioner for Patents, and
MICHAEL W. KIM, Vice ChiefAdministrative Patent Judge.

SQUIRES, Under Secretary ofCommerce for Intellectual Property and
Director ofthe United States Patent and Trademark Office.

              DECISION ON REQUEST FOR REHEARING

                         I.     INTRODUCTION
      This Appeals Review Panel ("ARP") was convened to review the
Board's Decision on Appeal ("Dec.") and Decision on Request for
Rehearing ("Reh'g Dec."), with particular focus on the Board's new ground
of rejection of claims 1-6 and 8-20 under 35 U.S.C. § 101. We have
jurisdiction under 35 U.S.C. § 6(b).

Appeal2024-000567
Application 16/319,040

      On review, we vacate the Board's new ground of rejection. We do not
disturb the Board's previous decisions in any other respects.

                           II.   BACKGROUND
      A. Claimed Invention
      Application No. 16/319,040 relates to training machine learning
models. Specification ("Spec.") ,r 2. Independent claim 1 reads:
           1.     A computer-implemented method of training a
      machine learning model,
             wherein the machine learning model has at least a plurality
      of parameters and has been trained on a first machine learning
      task using first training data to determine first values of the
      plurality of parameters of the machine learning model, and
             wherein the method comprises:
            determining, for each of the plurality of parameters, a
      respective measure of an importance of the parameter to the first
      machine learning task, comprising:
                    computing, based on the first values of the plurality
             of parameters determined by training the machine learning
             model on the first machine learning task, an approximation
             of a posterior distribution over possible values of the
             plurality of parameters,
                    assigning, using the approximation, a value to each
             of the plurality of parameters, the value being the
             respective measure of the importance of the parameter to
             the first machine learning task and approximating a
             probability that the first value of the parameter after the
             training on the first machine learning task is a correct
             value of the parameter given the first training data used to
             train the machine learning model on the first machine
             learning task;
             obtaining second training data for training the machine
      learning model on a second, different machine learning task; and

                                       2

Appeal2024-000567
Application 16/319,040

              training the machine learning model on the second
       machine learning task by training the machine learning model on
       the second training data to adjust the first values of the plurality
       of parameters to optimize performance of the machine learning
       model on the second machine learning task while protecting
       performance of the machine learning model on the first machine
       learning task,
              wherein adjusting the first values of the plurality of
       parameters comprises adjusting the first values of the plurality of
       parameters to optimize an objective function that depends in part
       on a penalty term that is based on the determined measures of
       importance of the plurality of parameters to the first machine
       learning task.
Appeal Br. 16 (Claims Appendix).
       The Specification discloses:
              Particular embodiments of the subject matter described in
       this specification can be implemented so as to realize one or more
       of the following advantages. By training the same machine
       learning model on multiple tasks as described in this
       specification, once the model has been trained, the model can be
       used for each of the multiple tasks with an acceptable level of
       performance. As a result, systems that need to be able to achieve
       acceptable performance on multiple tasks can do so while using
       less of their storage capacity and having reduced system
       complexity. For example, by maintaining a single instance of a
       model rather than multiple different instances of a model each
       having different parameter values, only one set of parameters
       needs to be stored rather than multiple different parameter sets,
       reducing the amount of storage space required while maintaining
       acceptable performance on each task. In addition, by training the
       model on a new task by adjusting values of parameters of the
       model to optimize an objective function that depends in part on
       how important the parameters are to previously learned task(s),
       the model can effectively learn new tasks in succession whilst
       protecting knowledge about previous tasks.
Spec. if 21.

                                        3

Appeal2024-000567
Application 16/319,040

      B. Procedural History
      On March 4, 2025, a Board panel issued a Decision on Appeal
(1) affirming the rejection of all pending claims 1-6 and 8-20 under
35 U.S.C. § 103 (one judge entered an opinion concurring-in-part, and
would have reversed this rejection), and (2) entering a new ground of
rejection of claims 1-6 and 8-20 under 35 U.S.C. § 101. On May 5, 2025,
the Appellant 1 filed a Request for Rehearing ("Req."), and addressed the
new ground of rejection. Req. 7-10. On July 14, 2025, the Board panel
issued a Decision on Request for Rehearing denying the Request in all
respects.
      C. Principles ofLaw and the Manual ofPatent Examining
         Procedure ("MP EP '')
      35 U.S.C. § 101 provides that "[w]hoever invents or discovers any
new and useful process, machine, manufacture, or composition of matter, or
any new and useful improvement thereof, may obtain a patent therefor."
Section 101, however, "contains an important implicit exception: Laws of
nature, natural phenomena, and abstract ideas are not patentable." Alice
Corp. Pty. Ltd. v. CLS Bankint'l, 573 U.S. 208,216 (2014) (quotingAss'n
for Molecular Pathology v. Myriad Genetics, Inc., 569 U.S. 576, 589
(2013)). Alice identifies a framework for determining whether claimed
subject matter is directed to an abstract idea. Id. at 21 7. According to Alice,
"[w]e must first determine whether the claims at issue are directed to a
patent-ineligible concept." Id. at 218 (emphasis added).

1
  The "Appellant" refers to the "applicant" as defined in 37 C.F.R. § l.42(a)
(2022). The Appellant identifies DeepMind Technologies Limited as the real
party in interest. Appeal Br. 1.
                                        4

Appeal2024-000567
Application 16/319,040

      Under Alice step one, we consider whether the claims at issue are
      directed to patent-ineligible subject matter, here, an abstract idea.
      This "directed to" inquiry does more than "simply ask whether
      the claims involve a patent-ineligible concept." Enfish, LLC v.
      Microsoft Corp., 822 F.3d 1327, 1335 (Fed. Cir. 2016) (emphasis
      in original). Instead, we must look to the character of the claims
      as a whole to determine whether they are "directed to" patent
      ineligible subject matter. Id.
AI Visualize, Inc. v. Nuance Commc 'ns, Inc., 97 F.4th 1371, 1378 (Fed. Cir.
2024). If so, the next step is "a search for an 'inventive concept'-i. e., an
element or combination of elements that is 'sufficient to ensure that the
patent in practice amounts to significantly more than a patent upon the
[ineligible concept] itself."' Alice, 573 U.S. at 217-18 (quoting Mayo
Collaborative Servs. v. Prometheus Labs., Inc., 566 U.S. 66, 72-73 (2012))
(alteration in original).
       The MPEP describes the process the Office follows in evaluating
whether a claim is drawn to patent-eligible subject matter under § 101. See
MPEP § 2106. Consistent with the statute, the process entails, at Step 1,
determining whether the claimed subject matter falls within one of the four
statutory categories of invention (i.e., process, machine, manufacture, or
composition of matter). See MPEP § 2106.03. Consistent with Alice's two
part framework, Step 2 of the process is a two-part test to identify whether
claims are directed to a judicial exception, i.e., an abstract idea, law of
nature, or natural phenomenon (Step 2A; see MPEP § 2106.04), and then to
evaluate if additional elements of the claim provide an inventive concept;
that is, whether they provide "significantly more" than the recited judicial
exception (Step 2B; see MPEP § 2106.05).
       Step 2A is a two-pronged inquiry. "Prong One asks does the claim
recite an abstract idea, law of nature, or natural phenomenon?" MPEP
                                        5

Appeal2024-000567
Application 16/319,040

§ 2106.04(II)(A)(l). "Prong Two asks does the claim recite additional
elements that integrate the judicial exception into a practical application?"
MPEP § 2106.04(II)(A)(2). Only after a determination is made that the claim
recites a judicial exception under the Prong One inquiry do we proceed to
the Prong Two inquiry, and then to Step 2B. "The Step 2A Prong One
analysis articulated in MPEP § 2106.04 ... requir[es] a claim to recite (i.e.,
set forth or describe) an abstract idea in Prong One before proceeding to the
Prong Two inquiry ...." MPEP § 2106.04(a)(l). If, at Prong Two, the claim
as a whole is not directed to a judicial exception, the eligibility analysis is
concluded. MPEP § 2106.04(II)(A)(2).

                               III.   ANALYSIS
      The Board's decisions and the Appellant's arguments focus on MPEP
Step 2A (Alice Step One). See Dec. 20-23; Req. 7-9; Reh'g Dec. 5-7.
Accordingly, we confine our discussion to Step 2A, as that resolves our

      A. Alice Step One; MP EP Step 2A, Prong One
      Independent claim 1 recites "computing ... , an approximation of a
posterior distribution over possible values of the plurality of parameters."
Independent claims 18 and 19 recite similar limitations. Appeal Br. 20-21
(Claims App.). In entering the new ground of rejection, the Board
determined that at least this limitation recites a mathematical calculation,
which is a mathematical concept, and, thus, an abstract idea. Dec. 20-21.
For this limitation, the Appellant neither disputed that the limitation recites
an abstract idea, nor identified the limitation as reciting features that confer
technical improvements. Req. 7-8. We see no reason to disturb this

                                        6

Appeal2024-000567
Application 16/319,040

undisputed finding, and so because independent claims 1, 18, and 19 each
recite at least one abstract idea, we proceed to the next part of our analysis
MPEP Step 2A, Prong Two.
      B. Alice Step One; MP EP Step 2A, Prong Two
      The Board determined next that "we discern no additional element (or
combination of elements) recited in Appellant's claims 1, 18, and 19 that
may have integrated the judicial exception into a practical application."
Dec. 22. The Appellant disagrees, asserting that "the claims recite additional
elements that reflect '[a]n improvement in the functioning of a computer, or
an improvement to other technology or technical field,' as discussed in
MPEP §§ 2106.04(d)(l) and 2106.05(a)." Req. 7. In particular, the
Appellant identifies certain limitations of independent claim 1 and asserts
that "the claimed subject matter provides technical improvements over
conventional systems by addressing challenges in continual learning and
model efficiency by reducing storage requirements and preserving task
performance across sequential training," citing paragraph 21 of the
Specification for support. Id. at 7-9; see also id. at 8 ("This training strategy
allows the model to preserve performance on earlier tasks even as it learns
new ones, directly addressing the technical problem of 'catastrophic
forgetting' in continual learning systems."). We agree with the Appellant.
      The determination requires us to "evaluate the significance of the
additional elements relative to the invention," while being mindful that "the
ultimate question" is "whether the exception is integrated into a practical
application." MPEP § 2106.04(d)(II). On the one hand, claims "[g]enerally
linking the use of a judicial exception to a particular technological
environment or field of use" are not patent eligible. See MPEP § 2106.05(h)

                                        7

Appeal2024-000567
Application 16/319,040

(citing Affinity Labs of Tex. v. DirecTV, LLC, 838 F .3d 1253 (Fed. Cir.
2016) and Elec. Power Grp., LLC v. Alstom SA., 830 F.3d 1350, 1354 (Fed.
Cir. 2016)). On the other, claims directed to an improvement in the
functioning of a computer, or an improvement to other technology or
technical field are patent eligible. See MPEP §§ 2106.04(d)(l) and
2106.05(a) (citing Enfish, LLC v. Microsoft Corp., 822 F.3d 1327, 1339
(Fed. Cir. 2016) andMcRO, Inc. v. Bandai Namco Games Am. Inc., 837
F.3d 1299, 1315 (Fed. Cir. 2016)).
      Enfish ranks among the Federal Circuit's leading cases on the
eligibility of technological improvements. In particular, Enfish recognized
that "[m ]uch of the advancement made in computer technology consists of
improvements to software that, by their very nature, may not be defined by
particular physical features but rather by logical structures and processes."
822 F.3d at 1339. Moreover, because "[s]oftware can make non-abstract
improvements to computer technology, just as hardware improvements can,"
the Federal Circuit held that the eligibility determination should turn on
whether "the claims are directed to an improvement to computer
functionality versus being directed to an abstract idea." Id. at 1336.
      Paragraph 21 of the Specification, which the Appellant cites,
identifies improvements in training the machine learning model itself. Of
course, such an assertion in the Specification alone is insufficient to support
a patent eligibility determination, absent a subsequent determination that the
claim itself reflects the disclosed improvement. See MPEP § 2106.05(a)
(citing Intellectual Ventures I LLC v. Symantec Corp., 838 F.3d 1307, 1316
(Fed. Cir. 2016)). Here, however, we are persuaded that the claims reflect
such an improvement. For example, one improvement identified in the

                                       8

Appeal2024-000567
Application 16/319,040

Specification is to "effectively learn new tasks in succession whilst
protecting knowledge about previous tasks." Spec. ,r 21. The Specification
also recites that the claimed improvement allows artificial intelligence (AI)
systems to "us[e] less of their storage capacity" and enables "reduced system
complexity." Id. When evaluating the claim as a whole, we discern at least
the following limitation of independent claim 1 that reflects the
improvement: "adjust the first values of the plurality of parameters to
optimize performance of the machine learning model on the second machine
learning task while protecting performance of the machine learning model
on the first machine learning task." We are persuaded that constitutes an
improvement to how the machine learning model itself operates, and not, for
example, the identified mathematical calculation.
      Under a charitable view, the overbroad reasoning of the original panel
below is perhaps understandable given the confusing nature of existing
§ 101 jurisprudence, but troubling, because this case highlights what is at
stake. Categorically excluding AI innovations from patent protection in the
United States jeopardizes America's leadership in this critical emerging
technology. Yet, under the panel's reasoning, many AI innovations are
potentially unpatentable-even if they are adequately described and
nonobvious-because the panel essentially equated any machine learning
with an unpatentable "algorithm" and the remaining additional elements as
"generic computer components," without adequate explanation. Dec. 24.
Examiners and panels should not evaluate claims at such a high level of
generality.
      However, it is with this view that the panel's sua sponte action is most
troubling, as it eschewed the clear teachings of Enfish, and instead

                                       9

Appeal2024-000567
Application 16/319,040

substituted only a cursory analysis that ignored this well-settled precedent.
Panels should treat such precedent with more care, especially when acting
sua sponte.
      At the same time, the claims at issue stand rejected under§ 103. This
case demonstrates that§§ 102, 103 and 112 are the traditional and
appropriate tools to limit patent protection to its proper scope. These
statutory provisions should be the focus of examination.
      For these reasons, we determine that although independent claim 1
may recite an abstract idea, it is not directed to an abstract idea. Instead, we
determine that independent claim 1, when considered as a whole, integrates
an abstract idea into a practical application. Our analysis is also applicable to
independent claims 18 and 19, and all pending dependent claims 2-6, 8-17,
and 20.

                             IV.   CONCLUSION
      In sum, we vacate the Board's New Ground of Rejection. We do not
disturb the Board's previous decisions in any other respects.

                      TIME PERIOD FOR RESPONSE
      No time period for taking any subsequent action in connection with
this appeal may be extended under 37 C.F.R. § l.136(a)(l)(iv).

                                       10
